import React from 'react'
import Accordion from 'react-bootstrap/Accordion';

// Import from files
import BarChart from '../charts/BarChart';
import PolarChart from '../charts/PolarChart';
import LineChart from '../charts/LineChart';
import RadarChart from '../charts/RadarChart';
import DoughnutChart from '../charts/DoughnutChart';
import PieChart from '../charts/PieChart';

const AccordionForCharts = ({ data }) => {
    return (
        <div>
            <Accordion>
                <Accordion.Item eventKey="0">
                    <Accordion.Header>Polar Area and Doughnut Charts - represents number of countries, sectors, topics, pestles, sources, etc are involved</Accordion.Header>
                    <Accordion.Body>
                        <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                            <PolarChart serverData={data} />
                            <DoughnutChart serverData={data} />
                        </div>
                    </Accordion.Body>
                </Accordion.Item>
                <Accordion.Item eventKey="1">
                    <Accordion.Header>Radar Chart - used for comparing multiple variables on the same scale</Accordion.Header>
                    <Accordion.Body>
                        <RadarChart serverData={data} />
                    </Accordion.Body>
                </Accordion.Item>
                <Accordion.Item eventKey="2">
                    <Accordion.Header>Line and Bar Charts - represents the continuous and categorical data</Accordion.Header>
                    <Accordion.Body>
                        <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                            <LineChart serverData={data} />
                            <BarChart serverData={data} />
                        </div>
                    </Accordion.Body>
                </Accordion.Item>
                <Accordion.Item eventKey="3">
                    <Accordion.Header>Pie Chart - depicts the relative contribution of different categories</Accordion.Header>
                    <Accordion.Body>
                        <PieChart serverData={data} />
                    </Accordion.Body>
                </Accordion.Item>
            </Accordion>
        </div>
    )
}

export default AccordionForCharts;
