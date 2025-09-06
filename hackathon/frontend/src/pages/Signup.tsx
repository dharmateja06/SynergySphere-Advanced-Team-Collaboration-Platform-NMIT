import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

function Signup() {
  const [form, setForm] = useState({ name: "", email: "", password: "" });
  const navigate = useNavigate();

  const handleSignup = (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: API signup
    navigate("/");
  };

  return (
    <div className="max-w-md mx-auto mt-20 bg-white shadow-lg p-6 rounded">
      <h2 className="text-2xl font-bold mb-4">Sign Up</h2>
      <form onSubmit={handleSignup} className="space-y-4">
        <input type="text" placeholder="Full Name"
          className="w-full border p-2 rounded"
          onChange={(e) => setForm({ ...form, name: e.target.value })} />
        <input type="email" placeholder="Email"
          className="w-full border p-2 rounded"
          onChange={(e) => setForm({ ...form, email: e.target.value })} />
        <input type="password" placeholder="Password"
          className="w-full border p-2 rounded"
          onChange={(e) => setForm({ ...form, password: e.target.value })} />
        <button className="w-full bg-green-600 text-white p-2 rounded">Sign Up</button>
      </form>
      <p className="mt-4 text-center">
        Already have an account? <Link to="/" className="text-blue-600">Login</Link>
      </p>
    </div>
  );
}

export default Signup;
