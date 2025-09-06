import { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

function CreateTask() {
  const { projectId } = useParams();
  const [form, setForm] = useState({ title: "", status: "Pending" });
  const navigate = useNavigate();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: API create task
    navigate(`/projects/${projectId}`);
  };

  return (
    <div className="max-w-md mx-auto bg-white p-6 shadow rounded">
      <h2 className="text-xl font-bold mb-4">Create Task</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input type="text" placeholder="Task Title" className="w-full border p-2 rounded"
          onChange={(e) => setForm({ ...form, title: e.target.value })} />
        <select className="w-full border p-2 rounded"
          onChange={(e) => setForm({ ...form, status: e.target.value })}>
          <option>Pending</option>
          <option>In Progress</option>
          <option>Completed</option>
        </select>
        <button className="w-full bg-green-600 text-white p-2 rounded">Create</button>
      </form>
    </div>
  );
}

export default CreateTask;
