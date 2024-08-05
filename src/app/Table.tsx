'use-client';

import { useState } from "react";
import axios from 'axios';
import { useEffect } from "react";


export default function Table(){
    const [items, setItems] = useState([]) ;   

    useEffect(() => {
        axios.get('http://localhost:5000/database')
            .then(response => {
                setItems(response.data);
            })
            .catch(error => {
                console.error("There was an error fetching the data!", error);
            });
    }, []);

        




    return ( 
        <div className="main">
        <table>
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Quantity</th>
                </tr>
            </thead>
            <tbody>
                {items.map((item, index) => (
                    <tr key={index}>
                        <td>{item.title}</td>
                        <td>{item.quantity}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>

);}






