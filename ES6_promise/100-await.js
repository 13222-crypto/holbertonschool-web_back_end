import { uploadPhoto, createUser } from './utils';

export default function asyncUploadUser() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photo, user]) => ({
      photo,
      user,
    }))
    .catch(() => ({
      photo: null,
      user: null,
    }));
}
