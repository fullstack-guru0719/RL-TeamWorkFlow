//Stringify an object by excluding the 'password' property.

const obj = {
  id: 1,
  username: 'KKK',
  password: 'secret',
  email: 'gillhousekevin@gmail.com',
};

JSON.stringify(obj, (key, value) => (key == 'password' ? undefined : value));

JSON.stringify(obj, ['id', 'username', 'email']);
