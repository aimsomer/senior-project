import axios, { AxiosResponse } from 'axios';

interface ScatterData {
  power: number;
  speed: number;
}

export async function fetchScatterData(): Promise<ScatterData[]> {
  try {
    const response: AxiosResponse<{ data: ScatterData[] }> = await axios.get('http://localhost:5000/api/scatter');
    return response.data.data;
  } catch (error) {
    console.log(error);
    return [];
  }
}
  