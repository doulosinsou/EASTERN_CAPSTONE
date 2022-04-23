let chart1 = false;
let chart2 = false;
let chart3 = false;
// let chart4 = false;

chart4 = [false,false,false,false]

window.onload=()=>{
    resort_dashboard()
}

// UPPER LEFT CHART

async function build_ul_chart(type,year,month,unique){
    const data = await fetchAPI('views-time',{'type':type,'year':year,'month':month,'unique':unique})
    let x 
    if (month){
        x = data.day
    }
    else if (year){
        console.log(data.month)
        const months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        x = []
        for (i=0;i<data.month.length;i++){
            x.push(months[data.month[i]-1]);
        }
    }
    else{
        x = data.year.map(String);
    }    

    const y = data.viewers;
    const label = 'Site '+type;

    draw_ul_chart(x,y,label)
}


function draw_ul_chart(xdata,ydata,label){
    
    const ul_data = {
        labels:xdata,
        datasets:[
            {
                label:label,
                borderColor:'rgb(255,99,132)',
                data:ydata
            }
        ]
    };

    const ul_config = {
        type:'line',
        data:ul_data,
        options: {
            plugins:{
                title:{
                    display:true,
                    text:label,
                    fullSize:true,
                    font:{
                        size:24,
                    }
                },
                legend:{
                    display:false,
                }
            }
        }
    }

    if (chart1){
        chart1.data.labels = xdata;
        chart1.data.datasets.forEach((dataset) => {
            dataset.data = ydata;
            dataset.label = label;
        });
        chart1.options.plugins.title.text = label
        chart1.update();
    }else{
        chart1 = new Chart(
            document.getElementById('ul-chart'),
            ul_config
        )

    }
}


// UPPER RIGHT KPI



async function build_ur_chart(year,month){
    year = false
    month = false
    data_av = await fetchAPI('kpi',{'request':'KPI_av','year':year,'month':month})
    data_goal = await fetchAPI('kpi',{'request':'KPI_goal','year':year,'month':month})
    
    
    kpi1 = document.getElementById('kpi1');
    kpi2 = document.getElementById('kpi2');
    draw_circle(kpi1,data_av.fillColor,data_av.kpi,'av views');
    draw_circle(kpi2,data_goal.fillColor,data_goal.kpi+'%','mo. goal');
}

function draw_circle(canvas,color,kpi,message){
    c = canvas.getContext('2d');
    c.beginPath();
    c.fillStyle='white';
    c.height = 250;
    c.width = 250;
    x = c.width / 2;
    y = c.height / 2;
    c.arc(x,y, 100, 0, 2*Math.PI, false);
    c.fill();

    c.lineWidth = 8;
    c.strokeStyle = color;
    c.stroke();

    c.beginPath();
    c.fillStyle='black';
    c.font = '40px Ariel';

    if (message=='av views'){
        c.fillText(kpi,x-23,y)
        c.font = '20px Ariel';
        c.fillText(message,x-32,y+40)
    }else{
        c.fillText(kpi,x-40,y)
        c.font = '20px Ariel';
        c.fillText(message,x-32,y+40)
    }
    c.fill()


}


// LOWER LEFT CHART

async function build_ll_chart(type,category,year,month){
    const data = await fetchAPI('views-type',{'type':type,'category':category,'year':year,"month":month})

    const label = type + ' by ' + category
    // const x = ['Jan','Feb','Mar','Apr','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    // const y = [0,10,5,2,20,30,45]

    const y = data.count_
    const x = data.cat_
    console.log(x,y)

    draw_ll_chart(x,y,label)
}


function draw_ll_chart(xdata,ydata,label){

    const ll_data = {
        labels:xdata,
        datasets:[
            {
                label:label,
                borderColor:'rgb(255,99,132)',
                data:ydata,
                backgroundColor:[
                    'rgba(54, 162, 235, 0.4)'
                ]
            }
        ]
    };

    const ll_config = {
        type:'bar',
        data:ll_data,
        options: {
            plugins:{
                title:{
                    display:true,
                    text:label,
                    fullSize:true,
                    font:{
                        size:24,
                    }
                },
                legend:{
                    display:false,
                }
            },
            indexAxis:'y',
        }
    };

    if (chart2){
        chart2.data.labels = xdata;
        chart2.data.datasets.forEach((dataset) => {
            dataset.data = ydata;
        });
        chart2.options.plugins.title.text = label
        chart2.update();
    }else{
        chart2 = new Chart(
            document.getElementById('ll-chart'),
            ll_config
        );
    }

};



// LOWER RIGHT CHART


async function build_lr_chart(type,year,month,unique){
    //Call for author list
    
    const data = await fetchAPI('authors',{'type':type,'year':year,'month':month,'unique':unique});
    const auth_stats_wrapper = document.getElementById('stats-author-wrapper');

    for (i=0;i<data.length;i++){
        let canvasID
        let row = data[i]
        if (!chart4[i]){
            let user_wrapper = document.createElement('div');
            let nid = "stats-"+row.author.replace(/\s/g,"-")
            user_wrapper.classList.add('stats-author');
            user_wrapper.id = nid;
            
            let img = make_avatar(row.avatar,1);
            let p_name = make_name(row.author,2);
            let [container,ID] = make_canvas(nid,3);
            let p_posts = make_post_stat(row.posts,4);
            let p_revenue = make_revenue_stat(row.revenue,5);

            let tags = [img,p_name,container,p_posts,p_revenue];
            for (j=0;j<tags.length;j++){
                user_wrapper.appendChild(tags[j]);
            canvasID = ID
            }
        auth_stats_wrapper.appendChild(user_wrapper);
        
        }

        let xdata = [...Array(row.views.month.length).keys()]
        let ydata = row.views.viewers
        
        draw_lr_chart(xdata,ydata,canvasID,i)

    }
}


function draw_lr_chart(xdata,ydata,domID,i){
    const lr_xLabs = xdata
    const lr_ycoord = ydata

    const lr_data = {
        labels:lr_xLabs,
        datasets:[
            {
                label:'',
                borderColor:'rgb(255,99,132)',
                data:lr_ycoord
            }
        ]
    };

    const lr_config = {
        type:'line',
        data:lr_data,
        options: {
            plugins:{
                title:{
                    display:false,
                    },
                legend:{
                    display:false,
                }
            },
            maintainAspectRatio:false,
            scales:{
                xAxis:{
                    display:false,
                },
                yAxis:{
                    display:false,
                }
            },
            elements:{
                point:{
                    radius: 0,
                }
            }
        }
    }
    
    if (chart4[i]){
        chart4[i].data.labels = lr_xLabs;
        chart4[i].data.datasets.forEach((dataset) => {
            dataset.data = lr_ycoord;
        });
        chart4[i].update();
    }else{
        const new_chart = new Chart(
            document.getElementById(domID),
            lr_config
        )
        chart4[i] = new_chart;
    }

}

function make_avatar(link,i){
    img = document.createElement('img');
    img.classList.add('stat-author-item','stat-author-item-'+i)
    linktext = "/img/"+link
    img.src = linktext;
    img.alt = "avatar from Pixabay.com";
    return img
}

function make_name(name,i){
    p = document.createElement('p');
    p.classList.add('stat-author-item','stat-author-item-'+i);
    p.innerText = name;
    return p
}

function make_post_stat(stat,i){
    p = document.createElement('p');
    p.classList.add('stat-author-item','stat-author-item-'+i);
    p.innerText = stat;
    return p
}

function make_revenue_stat(stat,i){
    p = document.createElement('p');
    p.classList.add('stat-author-item','stat-author-item-'+i);
    p.innerText = stat;
    return p
}

function make_canvas(nid,i){
    container = document.createElement('div');
    container.classList.add('stats-sparkline','stat-author-item','stat-author-item-'+i);
    canvas = document.createElement('canvas');
    canvas.id=nid+"-spark";
    container.appendChild(canvas);
    return [container, canvas.id]
}





function resort_dashboard(){

    let unique = document.getElementById('_type-all').value;
    let year = document.getElementById('sort-year').value 
    let month = document.getElementById('sort-month').value 
    const view_subs = document.getElementById('sort-graph').value 
    const top_tag = document.getElementById('sort-graph-2').value 

    if (unique == 'false'){
        unique = false;
    }else{
        unique = true;
    }
    if (year == 'false'){
        year = false;
    }else{
        year = parseInt(year);
    }
    if (month == 'false'){
        month = false;
    }else{
        month = parseInt(month);
    }

    build_ul_chart(view_subs,year,month,unique)
    build_ur_chart(year,month)
    build_ll_chart(view_subs,top_tag,year,month)
    build_lr_chart(view_subs,year,month,unique)
    



}