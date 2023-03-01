import React from 'react';
import './topbar.css';
import { NotificationsNoneIcon } from '@mui/icons-material';

export default function Topbar() {
  return (
    <div className="topbar">
      <div className="topbarWrapper">
        <div className="topLeft">
          <span className="logo">DigitalOcean</span>
        </div>
        <div className="topRight">
          <div className="topbarIconContainer">
            <NotificationsNoneIcon />
            <span className="topIconBag">2</span>
          </div>
        </div>
      </div>
    </div>
  );
}
