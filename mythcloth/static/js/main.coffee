$(document).ready ->
    total = 0

    # $('.highchart tbody').find('tr').each ->
    #     votes = $(this).find('td:nth-child(2)').html()
    #     total = total + parseInt(votes)
    #     return

    days = []

    $('.highchart thead').find('th').not(':nth-child(1)').each ->
        day = $(this).html()
        days.push(day)

    console.log('days')
    console.log(days)

    itemsData = []

    $('.highchart tbody').find('tr').each ->
        name = $(this).find('td:nth-child(1)').html()
        priceData = []
        $(this).find('td').not(':nth-child(1)').each ->
            price = $(this).html()
            price = parseFloat(price)
            # percent = (parseFloat(votes) / parseFloat(total)) * 100
            priceData.push(price);

        console.log('priceData')
        console.log(priceData)

        itemsData.push({
            name: name,
            data: priceData
        });

        return

    console.log('itemsData')
    console.log(itemsData)

    # Create the chart
    $('#highchart-container').highcharts
        # height: 600
        # chart: type: 'column'
        title:
            text: ''
        # xAxis:
        #     type: 'category'
        #     labels:
        #         style:
        #             fontSize:'16px'
        xAxis:
            categories: days
        # yAxis:
        #     title:
        #         text: ''
        yAxis:
            title:
                text: ''
            #  plotLines: [{
            #     value: 0,
            #     width: 1,
            #     color: '#808080'
            # }]
        # legend: enabled: false
        # plotOptions: series:
        #     borderWidth: 0
        #     dataLabels:
        #         enabled: true
        #         format: '{point.y:.1f}%'
        #         style:
        #             fontSize:'16px'
        # tooltip:
        #     enabled: false
        series: itemsData
        legend:
            layout: 'vertical'
            align: 'right'
            verticalAlign: 'middle'
            borderWidth: 0
        chart:
            height: 1500

