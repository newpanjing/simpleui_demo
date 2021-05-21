from django.db import models
from django import forms
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe


class Input:
    needs_multipart_form = False
    is_hidden = False
    attrs = {}
    is_required = False

    def get_context(self, name, value, attrs):
        context = {}
        context['widget'] = {
            'name': name,
            'is_hidden': self.is_hidden,
            'required': self.is_required,
            'value': self.format_value(value),
            'attrs': self.build_attrs(self.attrs, attrs),
            'template_name': self.template_name,
        }
        return context

    def format_value(self, value):
        """
        返回在模板中呈现时应该出现的值。
        """
        if value == '' or value is None:
            return None
        if self.is_localized:
            return formats.localize_input(value)
        return str(value)

    def value_from_datadict(self, data, files, name):
        """
        Given a dictionary of data and this widget's name, return the value
        of this widget or None if it's not provided.
        """
        return data.get(name)

    def id_for_label(self, id_):
        """
        给定字段的ID，返回此小部件的HTML ID属性，以供<label>使用。
        如果没有可用的ID，则返回None。
        这个钩子是必需的，因为一些小部件有多个HTML元素，因此有多个id。
        在这种情况下，这个方法应该返回一个ID值，该值对应于小部件标记中的第一个ID。
        """
        return id_

    def use_required_attribute(self, initial):
        return not self.is_hidden

    def build_attrs(self, base_attrs, extra_attrs=None):
        """Build an attribute dictionary."""
        return {**base_attrs, **(extra_attrs or {})}

    def value_omitted_from_data(self, data, files, name):
        return name not in data

    def get_bind_attr(self, attrs=None):
        """
        获取该控件需要绑定的变量参数
        :return:
        """
        if not attrs:
            self.bind_attr = {}
            return
        for key, value in attrs.items():
            if key[0] == ":":
                if isinstance(value, str):
                    self.bind_attr[value] = ''
                elif isinstance(value, dict):
                    for a, b in value.items():
                        self.bind_attr[a] = b
                else:
                    continue


class RateInput(forms.FloatField, Input):
    class Media:
        pass

    def __init__(self, max_value=5, allow_half=False, disabled=False, show_score=True, *args, **kwargs):
        super(RateInput, self).__init__(*args, **kwargs)
        self.max_value = max_value
        self.allow_half = allow_half
        self.disabled = disabled
        self.show_score = show_score

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ''

        return mark_safe(render_to_string('rate/rate.html', {
            'value': conditional_escape(force_text(value)),
            'name': name,
            'max_value': self.max_value,
            'allow_half': self.allow_half,
            'disabled': self.disabled,
            'show_score': self.show_score
        }))


class RateField(models.FloatField):

    def __init__(self, max_value=5, allow_half=False, disabled=False, show_score=True, *args, **kwargs):
        # 参数
        self.max_value = max_value
        self.allow_half = allow_half
        self.disabled = disabled
        self.show_score = show_score

        super(RateField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        r = super(RateField, self).formfield()
        r.widget = RateInput(self.max_value, self.allow_half, self.disabled, self.show_score)
        return r
