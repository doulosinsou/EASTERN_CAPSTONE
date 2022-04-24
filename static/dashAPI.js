async function fetchAPI(path,obj){
    const url = '/stats/'+path+'/';
    const call = await fetch(url,{
        method: 'POST',
        credentials:'same-origin',
        mode:'cors',
        headers: {
            'Content-Type':'application/json',
        },
        body: JSON.stringify(obj),
    })
    const parsed = await call.json()
    
    return parsed
}