

var socket = new WebSocket('ws://localhost:8000/ws/');
        socket.onmessage = function(event){
            var data = JSON.parse(event.data);
            

        var ppm_list = [
            'ppm_01', 'ppm_02', 'ppm_03', 'ppm_04', 'ppm_05', 'ppm_06', 'ppm_07', 'ppm_08', 'ppm_09', 'ppm_10', 
            'ppm_11', 'ppm_12', 'ppm_13', 'ppm_14', 'ppm_15', 'ppm_16', 'ppm_17', 'ppm_18', 'ppm_19', 'ppm_20',
        ]
        
        for (module in ppm_list){
            document.getElementById(ppm_list[module]).innerHTML = data.message['ppm'][ppm_list[module]];
        }


        // Modificar backgroud segun se activen las alarmas.
        var alarm_list = [
            'a_01', 'a_02', 'a_03', 'a_04', 'a_05', 'a_06', 'a_07', 'a_08', 'a_09', 'a_10', 
            'a_11', 'a_12', 'a_13', 'a_14', 'a_15', 'a_16', 'a_17', 'a_18', 'a_19', 'a_20',  
        ]

        for (element in alarm_list){

            if (data.message['alarm'][alarm_list[element]] == 1){
                typeof(alarm_list[element]);
                document.getElementById(alarm_list[element]).style.background = 'red';
                document.getElementById(alarm_list[element]).style.color = 'white'; 
            }
            else{
                document.getElementById(alarm_list[element]).style.background = 'green'; 
                document.getElementById(alarm_list[element]).style.color = 'white'; 
            }
        }


        // Modificar backgroud segun se activen las pre alarmas.
        var pre_alarm_list = [
            'p_01', 'p_02', 'p_03', 'p_04', 'p_05', 'p_06', 'p_07', 'p_08', 'p_09', 'p_10', 
            'p_11', 'p_12', 'p_13', 'p_14', 'p_15', 'p_16', 'p_17', 'p_18', 'p_19', 'p_20',  
        ]

        for (element in pre_alarm_list){

            if (data.message['pre_alarm'][pre_alarm_list[element]] == 1){
                typeof(alarm_list[element]);
                document.getElementById(pre_alarm_list[element]).style.background = 'red';
                document.getElementById(pre_alarm_list[element]).style.color = 'white'; 
            }
            else{
                document.getElementById(pre_alarm_list[element]).style.background = 'green'; 
                document.getElementById(pre_alarm_list[element]).style.color = 'white'; 
            }
        }
    }