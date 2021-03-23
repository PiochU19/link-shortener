import { useState } from 'react';
import './Main.scss';

const Main = () => {

	const [value, setValue] = useState("");
	const [short_url, set_short_url] = useState("");
	const [a_short_url, set_a_short_url] = useState("");

	const handleChange = e => {
		setValue(e.target.value);
	}

	const handleSubmit = async e => {
    	e.preventDefault()
    	try {
    		const request = await fetch(`http://localhost:8000/api/create/`, {
    			method: 'POST',
    			headers: {
                	'Accept': 'application/json, text/plain',
                	'Content-Type': 'application/json;charset=UTF-8'
            	},
    			body: JSON.stringify({"url": value})
    		});
      		const response = await request.json();

      		e.target.reset();

      		set_short_url('localhost:8000/'+ response.short_url);
      		set_a_short_url('http://localhost:8000/'+ response.short_url);

    	} catch (err) {
      		console.log(err);
    	}	
  	}

	return (
		<div className='Main'>
			{ short_url && <div className='Short-url'> <a href={a_short_url}>{short_url}</a> </div> }
			<div className='Form__group Field'>
				<form onSubmit={handleSubmit}>
					<input className='Form__field' type='text' id='url' placeholder='URL' onChange={handleChange} />
					<label for='url' className='Form__label'>URL</label>
				</form>
			</div>
		</div>
	);
};

export default Main;