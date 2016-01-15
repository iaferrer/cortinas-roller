jQuery('document').ready(function(){
  var page = $('#top-menu').attr('data-page');

  if (page === 'index'){
    $('#index').addClass('active');
  }else if (page === 'about'){
    $('#about').addClass('active');
  }else if (page === 'catalogue'){
    $('#catalogue').addClass('active');
  }else if (page === 'contact'){
    $('#contact').addClass('active');
  }

  var showing = false;
  $('.image-container a').click(function(e){
    e.preventDefault();
    var type = $(this).attr('data-type').toLowerCase();
    var element = this;
    $.ajax({
      type: "GET",
      url: "/products/"+ type +"/",
      dataType: "json",
      success: function(data){
        if (data['ok']){
          $('.image-container a').not(element).toggle('200');
          if (showing === false){
            $(element).parent().siblings().append(data['first_html']);
            $('#container-page').append(data['rest_html']);
            showing = true;
          }else {
            $("."+$(element).attr('data-type')).remove();
            $(".extra-row").remove();
            showing = false
          }
        }
      },
      error: function(data){
        alert('There was a server error, please try later.');
      }
	   });
  });

  $('form.message').on('submit', function(e){
    e.preventDefault();

    name = $('#name').val();
    email = $('#email').val();
    message = $('#message').val();

    if ((name !== '') && (email !== '') && (message !== '')){
      $.ajax({
        type: "POST",
        url: "/send_message/",
        data: {
          name: name,
          email: email,
          message: message
        },
        dataType: "json",
        success: function(data){
          alert("Mail Enviado Exitosamente.");
        },
        error: function(data){
          alert("Lo sentimos, hubo un error al enviar el mail.\n Inténtelo más tarde.");
        }
      })
    } else {
      alert("Porfavor completar todos los campos correctamente.");
    }
  })
});
