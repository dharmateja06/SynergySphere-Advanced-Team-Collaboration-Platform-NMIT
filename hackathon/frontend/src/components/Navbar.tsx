import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-blue-600 text-white p-4 flex justify-between">
      <h1 className="font-bold text-xl">Project Manager</h1>
      <div className="space-x-4">
        <Link to="/projects">Projects</Link>
        <Link to="/my-tasks">My Tasks</Link>
        <Link to="/">Logout</Link>
      </div>
    </nav>
  );
}

export default Navbar;
