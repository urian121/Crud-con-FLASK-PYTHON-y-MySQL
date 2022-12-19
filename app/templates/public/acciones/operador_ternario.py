 {% set saludar = 'hola' %}
            {{ 'H' if saludar =='hola' else 'N' }}
            {{ saludar =='hola' and 'Update' or 'Continue' }}
            con ninja 2
            
            {% if files %}
    Update
{% else %}
    Continue
{% endif %}