/** @odoo-module */

import { FormRenderer } from "@web/views/form/form_renderer";
import { FormView } from "@web/views/form/form_view";
import { Registry } from "@web/core/registry";
console.log("🔥 company_form.js loaded");

class CompanyFormRenderer extends FormRenderer {
    static template = "companies_extension.CompanyForm"
}

export const CompanyFormView = {
    ...FormView,
    Renderer: CompanyFormRenderer,
};
const viewRegistry = new Registry();
viewRegistry.category("views").add("company_form", CompanyFormView);
