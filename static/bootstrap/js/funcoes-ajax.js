function horaExtraUsada(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/hora-extra-usada/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            console.log(result)
            $("#mensagem").text('Hora Extra UTILIZADA!');
        }
    });
}