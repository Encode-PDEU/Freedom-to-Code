import React from "react";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

function ComplaintStatus() {
  return (<div>
    <h2>Complaint Status</h2>
    <Form>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Reference Number</Form.Label>
        <Form.Control type="number" placeholder="Enter Reference Number" />
        <Form.Text className="text-muted">
          Never share your Reference Number with anyone else.
        </Form.Text>
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control type="password" placeholder="Password" />
      </Form.Group>
     
      <Button variant="primary" style={{backgroundColor: "#138808", borderColor: "#0d6c04"
}} type="submit">
        Submit
      </Button>
    </Form>
    </div>
  );
}

export default ComplaintStatus;