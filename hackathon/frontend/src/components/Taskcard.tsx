type Task = {
  id: number;
  title: string;
  status: string;
};

type TaskCardProps = {
  task: Task;
};

const TaskCard: React.FC<TaskCardProps> = ({ task }) => (
  <div>
    <h3>{task.title}</h3>
    <p>{task.status}</p>
  </div>
);

export default TaskCard;
