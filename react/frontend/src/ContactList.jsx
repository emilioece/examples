import React from "react";

const ContactList = ({ contacts, updateContact, updateCallback }) => {
  const onDelete = async (id) => {
    try {
      const options = {
        method: "DELETE",
      };
      const response = await fetch(
        `http://127.0.0.1:5000/delete_contact/${id}`,
        options
      );
      if (response.ok) {
        updateCallback();
      } else {
        console.error("failed to delete");
      }
    } catch (error) {
      alert(error);
    }
  };
  return (
    <div>
      <h2>contacts</h2>

      <table>
        <thead></thead>
        <tr>
          <th>first name</th>
          <th>last name</th>
          <th>email</th>
          <th>actions</th>
        </tr>
        <tbody>
          {contacts.map((contact) => (
            <tr key={contact.id}>
              <td>{contact.firstName}</td>
              <td>{contact.lastName}</td>
              <td>{contact.email}</td>
              <td>
                <button onClick={() => updateContact(contact)}>update</button>
                <button onClick={() => onDelete(contact.id)}>delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ContactList;
