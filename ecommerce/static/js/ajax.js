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


// $(document).ready(function() {
//     $('.mdb-select').materialSelect();
//     });

    // function submit_review(){
        jQuery(document).on('click', '#p112', function (e) {

        // $('#p112').on('click', function(e) {

            e.preventDefault();
            var Text = $("#Text").val();
            var TextId = $("#pid").val();
            if(Text.length === 0){
                alert("\nPlease enter the feedback message!!!");
            }
            else{

            $.ajax({
                type: 'POST',
                url: "/review/prediction/",
                data: {Text: Text,TextId:TextId},

                success: function (data) {
                        // console.log(data);
                        var data_2 = "";
                        var data_1 = data;
                        var length = data_1.length;
                        var index = data_1.indexOf("jayitsaha")
                        data_2 = data_1.slice(0,index);
                        data_1 = data_1.slice(index+9,length);

                        $('#haha').html(data_2);
                        $('#hehe').html(data_1);
                        $("#Text").value = "";

                },
                error: function (response) {
                    // alert the error if any error occured
                    console.log(response);
                }


            })
        }
        })


    // }



