import { useState } from "react";
import { useNavigate } from "react-router-dom";

function CreateProject() {
  const [form, setForm] = useState({ name: "", description: "" });
  const navigate = useNavigate();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: API create project
    navigate("/projects");
  };

  return (
    <div className="max-w-md mx-auto bg-white p-6 shadow rounded">
      <h2 className="text-xl font-bold mb-4">Create Project</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input type="text" placeholder="Project Name" className="w-full border p-2 rounded"
          onChange={(e) => setForm({ ...form, name: e.target.value })} />
        <textarea placeholder="Description" className="w-full border p-2 rounded"
          onChange={(e) => setForm({ ...form, description: e.target.value })}></textarea>
        <button className="w-full bg-blue-600 text-white p-2 rounded">Create</button>
      </form>
    </div>
  );
}

export default CreateProject;
