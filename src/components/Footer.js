import './Footer.scss';
import boat from '../assets/img/boat.png';

const Footer = () => {
	return (
		<div className='Footer'>
			<div className='FooterText'>
				<h1>© Dominik Pioś 2021</h1>
			</div>
			<div className='BoatImg'>
				<img src={boat} alt='BoatImg' />
			</div>
		</div>
	);
};

export default Footer;