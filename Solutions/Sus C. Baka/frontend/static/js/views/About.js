import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
    constructor(params) {
        super(params);
        this.setTitle("Settings");
    }

    async getHtml() {
        return `
            <h1>About Us</h1>
            <p>This is a project made by Sus C. Baka as a means of
            giving back to the community that has done some much for them.
            The app was meant as a gift back to society
            by providing an easy and fast way for people to get in touch
            with the respective authorities, in order to efficiently take care of the problem</p>
        `;
    }
}