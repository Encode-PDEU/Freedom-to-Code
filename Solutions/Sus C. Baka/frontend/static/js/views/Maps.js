import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
    constructor(params) {
        super(params);
        this.setTitle("Submit A complaint");
    }

    async getHtml() {
        return`
        <script>
        jQuery(document).ready(function () {

            var map = new google.maps.Map($('#map')[0], {
                zoom: 5,
                center: new google.maps.LatLng(40.747688, -74.004142),
                mapTypeId: google.maps.MapTypeId.ROADMAP    
            });
            
            google.maps.event.addListener(map, 'click', function(e) {        
                var marker = new google.maps.Marker({
                    position: e["latLng"],
                    title:"Hello World!"
                });       
                marker.setMap(map);
            });        
        });
        </script>`
    }
}