class App extends React.Component {
    constructor(props) {
        super(props);
            this.state = {
            data: [],
            loaded: false,
            placeholder: "Loading"
        };
    }

    componentDidMount() {
        fetch("api/employees/")
            .then(response => {
                if (response.status > 400) {
                    return this.setState(() => {
                        return { placeholder: "Something went wrong!" };
                    });
                }
                return response.json();
            })
            .then(data => {
                this.setState(() => {
                    return {
                        data,
                        loaded: true
                    };
                });
            });
    }
    render() {
        return (
            <ul>
                {this.state.data.map((employee) => {
                    return (
                        <li key={employee.id}>
                            {employee.first_name} - {employee.email}
                        </li>
                    );
                })}
            </ul>
        );
    }
}

ReactDOM.render(
  <App />, document.getElementById('root')
);
