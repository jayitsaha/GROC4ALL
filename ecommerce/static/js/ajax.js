$(function(){

    $('#search').keyup(function(){
        var x = $('#search').val()
        if(x=='')
        {
            x = "NONE"
        }

        $.ajax({

            type:"POST",
            url:"search/",
            data:{
                'search_text':x,
                //  $('#search').val(),
                // 'csrfmiddlewaretoken':$("input|name=csrfmiddlewaretoken").val()

            },
            success:searchSuccess,
            dataType:'html',

        });
     });
});

function searchSuccess(data , textStatus,jqXHR)
{
    console.log(data)
    $('#search-results').html(data);
}


$(document).ready(function() {
    $('.mdb-select').materialSelect();
    });