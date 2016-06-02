/**
 * Created by wuilfred on 11/05/16.
 */

$.ajax({
    url : '/home/ticketEventSpecific/',
    type : 'GET',
    data: {id: '3920'},
    cache: true,
    contentType: "application/json",
    dataType : 'json',
    success : function(json) {
        console.log(json);
    },
    error : function(xhr, status) {
        console.log('error');
    },
    complete : function(xhr, status) {
        console.log('Petición realizada');
    }
});


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


$.ajax({
    url: '/home/ticketguestlist/',
    type: 'GET',
    data: { id: 3920 },
    cache: true,
    contentType: "application/json",
    dataType: 'json',
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    },
    success : function(json) {

        var user_text = "";
        var id_guest = "";
        var guest_email = "";
        var guest_event = "";
        for(var l = 0; l<json.user.length; l++){
            //  console.log(json.list_guest[l]);
            id_guest += json.list_guest[l].id + "<br>";
            user_text += json.user[l].first_name+'  '+json.user[l].last_name + "<br>";
            guest_email += json.list_guest[l].email + "<br>";
            guest_event += json.list_guest[l].event + "<br>";
            $('#guestid').html(id_guest);
            $('#guestuser').html(user_text);
            $('#guestemail').html(guest_email);
            $('#guestevent').html(guest_event);
        }
    },
    error : function(xhr, status) {
        console.log('error');
    },
    complete : function(xhr, status) {
        console.log('Petición realizada');
    }
});

