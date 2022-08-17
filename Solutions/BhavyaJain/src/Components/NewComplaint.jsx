import React from "react";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

function NewComplaint() {
  return (<div>
    <h2>New Complaint</h2>
    <Form>
    <Form.Group className="mb-3">
        <Form.Label>Complaint Type</Form.Label>
        <Form.Select>
        <option value="" disabled selected>Select Complaint Category</option>
          <option>Road</option>
          <option>Water</option>
          <option>Electricity</option>
          <option>Gas</option>
          <option>Mosquitoes</option>
          <option>Cleanliness</option>
          </Form.Select>
          </Form.Group>
          <Form.Group className="mb-3" >
            <Form.Label>Full Name</Form.Label>
            <Form.Control type="text" placeholder="Enter Your Full Name">
            </Form.Control>
          </Form.Group>
          <Form.Group className="mb-3" >
            <Form.Label>Address</Form.Label>
            <Form.Control as="textarea" placeholder="Enter Your Address">
            </Form.Control>
          </Form.Group>
          <Form.Group className="mb-3" >
            <Form.Label>Mobile Number</Form.Label>
            <Form.Control type="tel" placeholder="Enter Your Mobile Number">
            </Form.Control>
          </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Email address</Form.Label>
        <Form.Control type="email" placeholder="Enter email" />
        <Form.Text className="text-muted">
          We'll never share your email with anyone else.
        </Form.Text>
      </Form.Group>

      <Form.Group className="mb-3" >
            <Form.Label>Complaint</Form.Label>
            <Form.Control as="textarea" placeholder="Enter Your Complaint">
            </Form.Control>
          </Form.Group>
      
      <Button variant="primary" style={{backgroundColor: "#FF9933", borderColor: "#f68d24"} }  type="submit">
        Submit
      </Button>
    </Form>
    </div>
  );
}

export default NewComplaint;