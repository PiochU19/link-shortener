import { useState } from 'react';
import './Main.scss';

const Main = () => {

	const [value, setValue] = useState("");
	const [short_url, set_short_url] = useState("");
	const [err_msg, set_error] = useState("");
	const [copied, set_copied] = useState("");

	const handleChange = e => {
		setValue(e.target.value);
	}

	const handleSubmit = async e => {
    	e.preventDefault()
    	try {
    		const request = await fetch(process.env.REACT_APP_API_ENDPOINT, {
    			method: 'POST',
    			headers: {
                	'Accept': 'application/json, text/plain',
                	'Content-Type': 'application/json;charset=UTF-8'
            	},
    			body: JSON.stringify({"url": value})
    		});
      		const response = await request.json();

      		e.target.reset();
      		setValue("");

      		const stat = request.status;

      		if (stat === 201) {
				set_short_url('localhost:8000/'+ response.short_url);
				set_copied("");
      		} else if (stat === 400) {
      			set_short_url("");
      			set_copied("");
      			set_error('Enter valid URL');
      		} else if (stat === 429) {
            set_short_url("");
            set_copied("");
            set_error('You can only make 10 short URLs per day');
          }

    	} catch (error) {
    		e.target.reset();
    		set_short_url("");
    		set_copied("");
      		set_error('Something went wrong with our servers');
    	}	
  	}

  	const copy_to_clipboard = () => {
  		const e1 = document.createElement('textarea');
  		e1.value = short_url;
  		e1.setAttribute('readonly', '');
  		e1.style = {position: 'absolute', left: '-9999px'};
  		document.body.appendChild(e1);
  		e1.select();
  		document.execCommand("copy");
  		document.body.removeChild(e1);
  		set_copied(true);
  	}

	return (
		<div className='Main'>

			{ short_url ? <div className='Short-url'>{ copied ? <span className='Link-below'>Copied!</span> : <span className='Link-below'>Click link below to copy</span> } <br /><button onClick={copy_to_clipboard}>{short_url}</button></div> : <div className='Short-url'>{err_msg}</div> }
			<div className='Form__group Field'>
				<form onSubmit={handleSubmit}>
					<input className='Form__field' type='text' id='url' placeholder='URL' onChange={handleChange} />
					<label htmlFor='url' className='Form__label'>URL</label>
				</form>
			</div>
		</div>
	);
};

export default Main;