odoo.define('dgi.produccion.cientifica.custom_form_script', function (require) {
    "use strict";

    var FormController = require('web.FormController');

    FormController.include({
        renderButtons: function ($node) {
            this._super.apply(this, arguments);
            if (this.$buttons) {
                this.$buttons.find('#custom_button').on('click', this.proxy('customButtonClick'));
            }
        },

        customButtonClick: function () {
            // Función que se ejecutará al hacer clic en el botón personalizado
            this.do_notify('Mensaje Personalizado', '¡Botón personalizado clickeado!');
        },
    });
});
