import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import 'bootstrap/dist/css/bootstrap.css';
import {
	TextField,
	FormControl,
	InputLabel,
	Input,
	FormHelperText,
	Box,
  } from '@mui/material';


function App() {
	const {
		register,
		handleSubmit,
		watch,
		formState: { errors, isSubmitting },
	} = useForm();

	const [value, setValue] = useState('');
	const delay = (d) => {
		return new Promise((resolve, reject) => {
			setTimeout(() => {
				resolve()
			}, d * 1000);
		})
	}
	const onSubmit = async (data) => {
		console.log(data)
		try {
			let req = await fetch("http://localhost:8080/add", 
			{ 
				method: "POST",
				headers: {
					"Content-type": "application/json"
				},
				body: JSON.stringify(data)
			})
			let res = await req.text()
			setValue(JSON.parse(res).shortUrl)
		} catch (error) {
			console.log(error)
			setValue(null)
		}
	}

	return (
		<div className='body'>
			{isSubmitting && <div>Loading...</div>}
			<div className='form-container'>
				<form onSubmit={ handleSubmit(onSubmit) } >
					<label>Long URL :</label>
					<input placeholder='Enter your url here'{...register("longUrl", { required: true })} type='text' />
					{errors.longUrl && <span>This field is required</span>} {' '}
					<button type="submit">Shorten it</button>
					<br />
					<label>Short URL :</label> {value}
				</form>
			</div>
		</div>
	)

}

export default App;
