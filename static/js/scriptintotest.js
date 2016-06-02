/**
 * Created by wuilfred on 11/05/16.
 */

var username = "wuilfred@gmail.com";
var password = "1qaz2wsx";

function make_base_auth(user, password) {
  var tok = user + ':' + password;
  var hash = btoa(tok);
  return "Basic " + hash;
}

$.ajax({
    url : 'http://www.intoparty.com/rest/events/',
    headers: {
        "Authorization": "Basic " + btoa(username + ":" + password)
    },
    type : 'GET',
    contentType: "application/json",
    dataType : 'json',
    success : function(json) {
        for(var itera=0; itera<json.length; itera++){
            var muestra = json[itera];
            console.log(muestra);
            $('#ver').html(muestra);
            for(var zx=0; zx<muestra.event_products.length; zx++){
                console.log(muestra.event_products[zx]);
            }
        }


        //$('<h1/>').text(json.title).appendTo('body');
        //$('<div class="content"/>')
            //.html(json.html).appendTo('body');
}, // código a ejecutar si la petición falla;
    // son pasados como argumentos a la función
    // el objeto de la petición en crudo y código de estatus de la petición
    error : function(xhr, status) {
        //alert('Disculpe, existió un problema');
    },

    // código a ejecutar sin importar si la petición falló o no
    complete : function(xhr, status) {
        //alert('Petición realizada');
    }
});