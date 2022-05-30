Описание модулей
================

Эта страница сгенерирована автоматически [#f1]_.

.. toctree::
   :titlesonly:

   {% for page in pages %}
   {% if page.top_level_object and page.display %}
   {{ page.include_path }}
   {% endif %}
   {% endfor %}

.. [#f1] Создано `sphinx-autoapi <https://github.com/readthedocs/sphinx-autoapi>`_
