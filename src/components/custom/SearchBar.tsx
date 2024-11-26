import { Group, Input, Button } from '@chakra-ui/react'
import { FaSearch } from 'react-icons/fa'

export function SearchBar(): JSX.Element {
  return (
    <Group>
      <Input placeholder="Search ..." />
      <Button variant="ghost"><FaSearch/></Button>
    </Group>
  )
}