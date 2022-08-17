import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
    constructor(params) {
        super(params);
        this.setTitle("Submit A complaint");
    }

    async getHtml() {
        return `
        <h1>Submit a Complaint</h1>
        <h2> Select a Category \n</h2>
          <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
          <link href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/css/select2.min.css" rel="stylesheet"/>
          <script src="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.full.min.js"></script>
          
          <select class="custom-select2" id = 'checklist'>
            <option value="SE">--Select--</option>
              <option value="TR">Trash pickup required</option>
              <option value="DW">Dirty water collected</option>
              <option value="DC">Disease carrying animals/Insects Spotted</option>
              <option value="OT">Other</option>
              <script>console.log(value)</script>
          </select>
          <button id="theButton" onclick="clickMe()">Click to select</button>
          <input type="text" name="popup" id="popup" class="hide" placeholder="Please explain in short">
          <button name="submit-button" id="submit-button" onclick="selectLocationShow()&mapViewShow()" hidden = 'true'>Confirm</button>
          <p>\n</p>
          <img id = "mapview" src = "/static/assets/earthview_with_marker.png" hidden></img>
          <p>\n</p>
          <button id = "select_location" onclick="showUpload()&showUploadButton()" hidden>Select Location (Backend not established)</button>
          <form id="upload" hidden ='true'>
	        <label id = file2 for="file">File to upload</label>
	        <input type="file" id="file" accept="image/*">
          </form>
	        <button id = "upload-button" onclick="location.href='./success'" hidden>Upload</button>
        `;
    }
}