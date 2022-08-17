import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
    constructor(params) {
        super(params);
        this.setTitle("Dashboard");
    }

    async getHtml() {
        return `
            <h1>Hello, and Welcome to the Swachh Bharat Mission app.</h1>
            <p>To lodge an official complaint, click on the following link, or use the main menu</p>
            <a href = "./submit">Click Here</a>
            
        `;
    }
}