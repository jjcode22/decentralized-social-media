import Image from 'next/image';
import Link from 'next/link';
import { Blockie } from '@web3uikit/web3';
import { AuthorContainer, AvatarEl } from './styled/Follow.styled';
import {useRouter} from 'next/router';

const Follow = ({ user }) => {
	const router = useRouter();

	return (
		<div onClick={() => router.reload(`/profile?id=${user._id}`)}>
			<AuthorContainer>
				<AvatarEl>
					<Blockie seed={user.address} size={10} />
				</AvatarEl>
				<span>
					{user.username}
				</span>
			</AuthorContainer>
		</div>
	);
};

export default Follow;
