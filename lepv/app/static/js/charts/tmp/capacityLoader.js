/*
 * Open source under the GPLv2 License or later.
 * Copyright (c) 2016, Mac Xu <shinyxxn@hotmail.com>.
 */

var CapacityLoader = (function(){
    
    var server;
    var requestId;
    var responseId = 0;

    var config = 'release';
    
    var componentDivMap = {};

    function _init() {
    }

    function setComponent(componentName, divName) {
        if(divName.indexOf("#") != 0) {
            divName = '#' + divName;
        }
        
        componentDivMap[componentName.toLowerCase()] = divName;
    }

    function loadMemoryCapacityInfo(data, divName) {
        Cookies.set('memory.total.' + server, data['capacity']);
        Cookies.set('memory.unit.' + server, data['unit']);

        $(divName).empty();

        var ulElement = $("<ul></ul>").addClass('list-group');
        var liElement1 =  $("<li></li>").addClass('list-group-item').text('内存: ' + data['summary']);
        ulElement.append(liElement1);

        $(divName).append(ulElement);
    }
    
    function loadCpuCapacityInfo(data, divName) {

        Cookies.set('cpu.cores.' + server, data['coresCount']);

        $(divName).empty();

        var ulElement = $("<ul></ul>").addClass('list-group');
        var liElement1 =  $("<li></li>").addClass('list-group-item').text('CPU: ' + data['summary'] + " ");
        
        var imgElement = $("<img></img>").addClass("logo-icon");
        if (data['architecture'] == "ARM") {
            imgElement.attr("src", "/static/images/arm.jpg");
        } else {
            imgElement.attr("src", "/static/images/x86.png");
        }
        liElement1.append(imgElement);
        
        var liElement2 =  $("<li></li>").addClass('list-group-item').text('Model: ' + data['model']);
        var liElement3 =  $("<li></li>").addClass('list-group-item').text("bogoMIPS: " + data['bogomips']);
        ulElement.append(liElement1, liElement2, liElement3);

        $(divName).append(ulElement);
    }

    function loadIOCapacityInfo(data, divName) {

        $(divName).empty();

        var ulElement = $("<ul></ul>").addClass('list-group');
        var liElement1 =  $("<li></li>").addClass('list-group-item').text('磁盘总容量: ' + data['diskTotal']);
        var liElement2 =  $("<li></li>").addClass('list-group-item').text('空闲磁盘空间: ' + data['diskUsed']);
        ulElement.append(liElement1, liElement2);

        $(divName).append(ulElement);
    }
    
    function start(serverToMonitor) {
        
        if (server == serverToMonitor) {
            return;
        }
        
        server = serverToMonitor;
        requestId = 0;
        responseId = 0;
        
        _init();

        // calculate the ratio of each type.
        $.each( componentDivMap, function( component, divName ) {
//            var url = "/capacity/" + component + "/" + server;

            var url = "api/" + component + "/capacity/" + server;
            $(divName).empty();
            
            $.get(url, function(responseData, status){
                if (component == "cpu") {
                    loadCpuCapacityInfo(responseData['data'], divName);
                } else if (component == "memory") {
                    loadMemoryCapacityInfo(responseData['data'], divName);
                } else if (component == "io") {
                    loadIOCapacityInfo(responseData['data'], divName);
                }
            });
        });
    }

    function setRunConfig(newConfig) {
        if (newConfig == 'debug') {
            config = newConfig;
        } else {
            config = 'release';
        }
    }
    
    return {
        setComponent: setComponent,
        setRunConfig:setRunConfig,
        start: start
    };

})();