const API = 'https://api.github.com/users';
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: 'lingeshwaran05',
      name: '',
      avatar: '',
      location: '',
      repos: '',
      followers: '',
      following: '',
      homeUrl: '',
      notFound: '' };

  }
  fetchProfile(username) {
    let url = `${API}/${username}`;
    fetch(url).
    then(res => res.json()).
    then(data => {
      this.setState({
        username: data.login,
        name: data.name,
        avatar: data.avatar_url,
        location: data.location,
        repos: data.public_repos,
        followers: data.followers,
        following: data.following,
        homeUrl: data.html_url,
        notFound: data.message });

    }).
    catch(error => console.log('Oops! . There Is A Problem'));
  }
  componentDidMount() {
    this.fetchProfile(this.state.username);
  }
  render() {
    return /*#__PURE__*/(
      React.createElement("div", null, /*#__PURE__*/
      React.createElement("section", { id: "card" }, /*#__PURE__*/
      React.createElement(SearchProfile, { fetchProfile: this.fetchProfile.bind(this) }), /*#__PURE__*/
      React.createElement(Profile, { data: this.state }))));



  }}

class SearchProfile extends React.Component {
  render() {
    return /*#__PURE__*/(
      React.createElement("div", { className: "search--box" }, /*#__PURE__*/
      React.createElement("form", { onSubmit: this.handleForm.bind(this) }, /*#__PURE__*/
      React.createElement("label", null, /*#__PURE__*/React.createElement("input", { type: "search", ref: "username", placeholder: "Type Username + Enter" })))));



  }

  handleForm(e) {
    e.preventDefault();
    let username = this.refs.username.getDOMNode().value;
    this.props.fetchProfile(username);
    this.refs.username.getDOMNode().value = '';
  }}


class Profile extends React.Component {
  render() {
    let data = this.props.data;
    let followers = `${data.homeUrl}/followers`;
    let repositories = `${data.homeUrl}?tab=repositories`;
    let following = `${data.homeUrl}/following`;
    if (data.notFound === 'Not Found')
    return /*#__PURE__*/(
      React.createElement("div", { className: "notfound" }, /*#__PURE__*/
      React.createElement("h2", null, "Oops !!!"), /*#__PURE__*/
      React.createElement("p", null, "The Component Couldn't Find The You Were Looking For . Try Again ")));else



    return /*#__PURE__*/(
      React.createElement("section", { className: "github--profile" }, /*#__PURE__*/
      React.createElement("div", { className: "github--profile__info" }, /*#__PURE__*/
      React.createElement("a", { href: data.homeUrl, target: "_blank", title: data.name || data.username }, /*#__PURE__*/React.createElement("img", { src: data.avatar, alt: data.username })), /*#__PURE__*/
      React.createElement("h2", null, /*#__PURE__*/React.createElement("a", { href: data.homeUrl, title: data.username, target: "_blank" }, data.name || data.username)), /*#__PURE__*/
      React.createElement("h3", null, data.location || 'I Live In My Mind')), /*#__PURE__*/

      React.createElement("div", { className: "github--profile__state" }, /*#__PURE__*/
      React.createElement("ul", null, /*#__PURE__*/
      React.createElement("li", null, /*#__PURE__*/
      React.createElement("a", { href: followers, target: "_blank", title: "Number Of Followers" }, /*#__PURE__*/React.createElement("i", null, data.followers), /*#__PURE__*/React.createElement("span", null, "Followers"))), /*#__PURE__*/

      React.createElement("li", null, /*#__PURE__*/
      React.createElement("a", { href: repositories, target: "_blank", title: "Number Of Repositoriy" }, /*#__PURE__*/React.createElement("i", null, data.repos), /*#__PURE__*/React.createElement("span", null, "Repositoriy"))), /*#__PURE__*/

      React.createElement("li", null, /*#__PURE__*/
      React.createElement("a", { href: following, target: "_blank", title: "Number Of Following" }, /*#__PURE__*/React.createElement("i", null, data.following), /*#__PURE__*/React.createElement("span", null, "Following")))))));





  }}


React.render( /*#__PURE__*/React.createElement(App, null), document.body);