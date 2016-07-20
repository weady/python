function alertType() {
        $.ajax( {

            url: "/monitor/command/", //'{% url 'command' %}'
            type: "POST",
            data: {
                cmd:$("#command").val(),
                host_name:$("#host_name").val()
            },
            dataType: "html",

            success: function ( res ) {             

                 $('#result').val( res );
             },
            error: function ( res ) {

             }
        } );
}
