/** @odoo-module **/

import { NavBar } from "@web/webclient/navbar/navbar";
import { patch } from "@web/core/utils/patch";
import { useState } from "@odoo/owl";

patch(NavBar.prototype, {
    setup() {
        super.setup();
        this.state = useState({
            ...this.state,
            isSidebarExpanded: localStorage.getItem('fewa_sidebar_expanded') === 'true',
        });
    },

    toggleSidebar() {
        this.state.isSidebarExpanded = !this.state.isSidebarExpanded;
        localStorage.setItem('fewa_sidebar_expanded', this.state.isSidebarExpanded);

        // Update a CSS variable on the root for layout adjustment
        const width = this.state.isSidebarExpanded ? '250px' : '70px';
        document.documentElement.style.setProperty('--fewa-sidebar-width', width);
    }
});
