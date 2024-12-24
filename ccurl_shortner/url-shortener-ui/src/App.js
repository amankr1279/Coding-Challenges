import './App.css';
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import 'bootstrap/dist/css/bootstrap.css';
import {
	TextField,
	Typography,
	Box,
	Button} from '@mui/material';


function App() {
	const {
		register,
		handleSubmit,
		watch,
		formState: { errors, isSubmitting },
	} = useForm();

	const [value, setValue] = useState("");
	const delay = (d) => {
		return new Promise((resolve, reject) => {
			setTimeout(() => {
				resolve()
			}, d * 1000);
		})
	}
	const onSubmit = async () => {
		let data = document.getElementById("longUrl").value;
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
			let res = await req.json()
			setValue(res.shortUrl)
			console.log(res)
		} catch (error) {
			console.log(error)
			setValue(null)
		}
	}

	return (
		<Box
			component="form"
			sx={{ '& > :not(style)': { m: 1, width: '25ch' } }}
			noValidate
			autoComplete="off"
			display="flex"
			flexDirection="column"
			maxWidth={1000}
			alignItems={'center'}
			justifyContent={"center"}
			margin={"auto"}
			marginTop={5}
			onSubmit={handleSubmit(onSubmit)}>

			<Typography variant='h2' padding={3} textAlign='center' >URL Shortener</Typography>
			<div style={{display: "inline-flex"}}>
			<TextField
				margin='none'
				variant='outlined'
				placeholder='Paste your url here'
				name='longUrl'
				id='longUrl'
				fullWidth
				type='text' />
			</div>
			{errors.longUrl && <span>This field is required</span>} {' '}
			<Button
				variant='contained'
				type="submit">Shorten it
			</Button>
			
			<TextField
				margin='normal'
				label="Shortened URL"
				variant="standard"
				color="warning"
				aria-readonly
				value={value}
			/>
		</Box>
	)

}

export default App;
