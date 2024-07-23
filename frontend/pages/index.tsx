import * as React from 'react';
import UploadComponent from '../components/UploadComponent';
import { Container, AppBar, Toolbar, Typography } from '@mui/material';

export default function Home() {
  return (
    <Container maxWidth="md">
      <AppBar position="static" sx={{ mb: 4 }}>
        <Toolbar>
          <Typography variant="h6">RAG System</Typography>
        </Toolbar>
      </AppBar>
      <UploadComponent />
    </Container>
  );
}
