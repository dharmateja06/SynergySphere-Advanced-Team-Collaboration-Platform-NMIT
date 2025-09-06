// src/pages/ProjectDetail.tsx
import "react";
import { useParams, Link } from "react-router-dom";
import TaskCard from "../components/Taskcard";        // <-- Make sure file name case matches
import Commentthread from "../components/Commentthread"; // <-- Make sure file name case matches

const ProjectDetails: React.FC = () => {
  const params = useParams<{ projectId: string }>();
  const projectId = params.projectId;

  if (!projectId) return <div>Project not found</div>;

  const numericProjectId = Number(projectId);
  if (isNaN(numericProjectId)) return <div>Invalid project ID</div>;

  return (
    <div>
      <h1>Project Details: {numericProjectId}</h1>
      <Link to="/projects" className="text-blue-500">
        Back to Projects
      </Link>

      <TaskCard task={{ id: 1, title: "Sample Task", status: "pending" }} />

      <Commentthread
  comments={[]}                // <-- fix here
  onAdd={() => console.log("Add comment")}
  projectId={numericProjectId}
/>

    </div>
  );
};

export default ProjectDetails;
