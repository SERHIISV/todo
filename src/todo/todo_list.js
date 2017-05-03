import React, {Component, PropTypes} from 'react'

class TodoList extends Component {

    render() {
        const {todos} = this.props

        const todoElements = todos.map((todo) => <li key={todo.id}>
            <Todo>
        </li>)

        return (
            <ul>
                {todoElements}
            </ul>
        )
    }
}

TodoList.propTypes = {
    todos: PropTypes.array.isRequired
}

TodoList.defaulyProps = {
    todos: []
}
