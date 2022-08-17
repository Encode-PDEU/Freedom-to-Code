import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
    constructor(params) {
        super(params);
        this.postId = params.id;
        this.setTitle("Successfully lodged complaint");
    }

    async getHtml() {
        return `
            <h1>Thank you for your assistance</h1>
            <h2>Your complaint has been lodged, and the authorities will look into it as soon as possible</h2>
            <a href = "./dashboard">Click to return to Dashboard</a>
        `;
    }
}
