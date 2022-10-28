import React,{useState} from 'react'
import './App.css';

function App() {
  const api={
    accessToken:"f16a131dbcb4e09ba1d6288ab3c8ea2540ff8da7",
  }
  
  const [searchInput, setSearchInput] = useState("");
  const [data,setData]=useState({});
	const [valid, setValidUrl] = useState(true);

	async function postUrl(url) {
		const res = await fetch("https://api-ssl.bitly.com/v4/shorten", {
			method: "POST",
			headers: {
				Authorization:
        `Bearer ${api.accessToken}`,
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				long_url: `${url}`,
			}),
		});

		return res.json();
	}

	function validURL(str) {
		var pattern = new RegExp(
			"^(https?:\\/\\/)?" + // protocol
				"((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|" + // domain name
				"((\\d{1,3}\\.){3}\\d{1,3}))" + // OR ip (v4) address
				"(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*" + // port and path
				"(\\?[;&a-z\\d%_.~+=-]*)?" + // query string
				"(\\#[-a-z\\d_]*)?$",
			"i"
		); // fragment locator
		return !!pattern.test(str);
	}

	function handleInput(e) {
		setSearchInput(e.target.value);
	}

	function handleFormSubmit(e) {
		e.preventDefault();
		if (validURL(searchInput)) {
			postUrl(searchInput).then((data) => {
				console.log(data);
				setData(data);
			});
		} else {
			setValidUrl(!valid);
      setData({});
			setTimeout(() => {
				setValidUrl(true);
			}, 2000);
		}
	}

	return (
		<div className='app'>
			<form className='formBox' onSubmit={handleFormSubmit}>
				<input
					value={searchInput}
					onChange={handleInput}
					placeholder="Enter url..."
				/>

				<button>Shorten</button>
			</form>
      {(valid)?<a className='linkBox' href={data?.link}>{data?.link}</a>:<p className='warning'>Please input a valid URL!!!!</p>}
      
			
		</div>
	);
};


export default App;
