import './widgetSm.css';
import { Visibility } from '@mui/icons-material';
export default function WidgetSm() {
  return (
    <div className="widgetSm">
      <span className="widgetSmTitle">New Join Member</span>
      <ul className="widgetSmList">
        <li className="widgetSmListItem">
          <img src="" alt="" className="widgetSmImg"></img>
          <div className="widgetSmUser">
            <span className="widgetSmUsername">Kevin Gillhouse</span>
            <span className="widgetSmUserTitle">Software Engineer</span>
          </div>
          <button className="widgetSmButton">
            <Visibility className="widgetSmIcon" />
            Display
          </button>
        </li>
        <li className="widgetSmListItem">
          <img src="" alt="" className="widgetSmImg"></img>
          <div className="widgetSmUser">
            <span className="widgetSmUsername">Kevin Gillhouse</span>
            <span className="widgetSmUserTitle">Software Engineer</span>
          </div>
          <button className="widgetSmButton">
            <Visibility className="widgetSmIcon" />
            Display
          </button>
        </li>
        <li className="widgetSmListItem">
          <img src="" alt="" className="widgetSmImg"></img>
          <div className="widgetSmUser">
            <span className="widgetSmUsername">Kevin Gillhouse</span>
            <span className="widgetSmUserTitle">Software Engineer</span>
          </div>
          <button className="widgetSmButton">
            <Visibility className="widgetSmIcon" />
            Display
          </button>
        </li>
        <li className="widgetSmListItem">
          <img src="" alt="" className="widgetSmImg"></img>
          <div className="widgetSmUser">
            <span className="widgetSmUsername">Kevin Gillhouse</span>
            <span className="widgetSmUserTitle">Software Engineer</span>
          </div>
          <button className="widgetSmButton">
            <Visibility className="widgetSmIcon" />
            Display
          </button>
        </li>
      </ul>
    </div>
  );
}
