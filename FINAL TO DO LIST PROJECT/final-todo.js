const Todo_list = [];


function addTodo(){
    inputTodoElement = document.querySelector('#todo');
    inputTodoDueDate = document.querySelector('#todo_due_date');
    todoName = inputTodoElement.value;
    dueDate = inputTodoDueDate.value;
    inputTodoElement.value = '';
    Todo_list.push({
        todoName,
        dueDate});
    // console.log(todo);
    // console.log(Todo_list);
    renderTodo();
}
document.querySelector('.add_btn').addEventListener('click', () => {
    addTodo()
});

function renderTodo(){
    let todoContainerHTML = '';
    todoContainer = document.querySelector('.js_todo_container');
    // for(let i=0;i<Todo_list.length;i++){
    //     let {todoName,dueDate} = Todo_list[i];
    //     let todoHTML = `
    //         <div>${todoName}</div> 
    //         <div>${dueDate}</div> 
    //         <button class = 'delete_btn btn'
    //             onclick = '
    //             Todo_list.splice(${i},1);
    //             renderTodo();'>
    //             Delete
    //         </button>`;
    //     todoContainerHTML += todoHTML;
    // }
    Todo_list.forEach((todoObj,index) => {
        let {todoName,dueDate} = todoObj;
        let todoHTML = `
            <div>${todoName}</div> 
            <div>${dueDate}</div> 
            <button class = 'delete_btn btn'
                onclick = '
                Todo_list.splice(${index},1);
                renderTodo();'>
                Delete
            </button>`;
        todoContainerHTML += todoHTML;
    })
    todoContainer.innerHTML = todoContainerHTML;
}


// function deleteTodo(event){
//     for(let i=0;i<Todo_list.length;i++){
//         if(event.target.parentNode.childNodes[1].innerText == i){
//             Todo_list.splice(i,1);
//             console.log(Todo_list);
//         }
//     }
//     event.target.parentNode.parentNode.removeChild(event.target.parentNode);
// }