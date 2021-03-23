import './Footer.scss';
import boat from '../assets/img/boat.png';

const Footer = () => {
	return (
		<div className='Footer'>
			<h1 className='FooterText'>© Dominik Pioś 2021</h1>
			<img className='BoatImg' src={boat} />
		</div>
	);
};

export default Footer;